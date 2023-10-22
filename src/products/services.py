from django.db.models.query import QuerySet

from abc import ABC, abstractmethod
from typing import Optional
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import Product


class IRecommendationProductService(ABC):

    @abstractmethod
    def get_recommendations(self, product_id: int) -> list[int]:
        pass


class RecommendationProductService(IRecommendationProductService):

    def __init__(self, products: QuerySet, field: str):
        self.field = field
        self.products = products
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.df = self.__get_df()
        self.tfidf = self.vectorizer.fit_transform(self.df[self.field])

    def get_recommendations(self, product_id: int, limit: int) -> list[int]:
        product = self.__get_product(product_id)
        if product is not None and not product.empty:
            index, description = self.__get_index_and_description(product)
            query_vec = self.vectorizer.transform([description])
            similarity = cosine_similarity(query_vec, self.tfidf).flatten()
            normalized_limit = self.__get_normalized_limit(limit, len(self.products))
            indexes = np.argpartition(similarity, normalized_limit)[normalized_limit:]
            filtered_indexes = list(filter(lambda i: i != index, indexes.tolist()))
            results = self.df.iloc[filtered_indexes].iloc[::-1]
            filtered_ids = results['id'].tolist()
            return filtered_ids
        return []

    def __get_index_and_description(self, product: DataFrame) -> tuple[int, str]:
        index = product.index[0]
        description = product.values[0][1]
        return index, description

    def __get_product(self, product_id: int) -> Optional[DataFrame]:
        try:
            product = self.df.loc[self.df['id'] == product_id]
        except KeyError:
            product = None
        return product

    def __get_df(self) -> DataFrame:
        df = pd.DataFrame(list(self.products))
        return df

    def __get_normalized_limit(self, limit: int, max: int) -> int:
        if limit > max:
            limit = max
        limit += 1  # To exclude the product itself
        return -1 * limit


def get_recommendation_service(
        field: str = 'description'
    ) -> IRecommendationProductService:
    products = Product.objects.all().values('id', 'description')
    instance = RecommendationProductService(products, field)
    return instance
