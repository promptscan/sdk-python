# Generated by ariadne-codegen
# Source: graphql/operations.gql

from typing import Any, Dict, List, Optional, Union

from .api_key import ApiKey
from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .collect_generations import CollectGenerations
from .input_types import GenerationInput


def gql(q: str) -> str:
    return q


class GraphQLClient(BaseClient):
    def collect_generations(
        self,
        generations: List[GenerationInput],
        project_id: Union[Optional[Any], UnsetType] = UNSET,
        **kwargs: Any
    ) -> CollectGenerations:
        query = gql(
            """
            mutation collectGenerations($generations: [GenerationInput!]!, $projectId: UUID) {
              collect(generations: $generations, projectId: $projectId) {
                success
                error {
                  message
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "generations": generations,
            "projectId": project_id,
        }
        response = self.execute(
            query=query,
            operation_name="collectGenerations",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return CollectGenerations.model_validate(data)

    def api_key(self, **kwargs: Any) -> ApiKey:
        query = gql(
            """
            query apiKey {
              apiKey {
                name
                scope
                createdTs
                enabled
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = self.execute(
            query=query, operation_name="apiKey", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ApiKey.model_validate(data)
