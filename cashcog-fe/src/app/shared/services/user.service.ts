import { Injectable } from '@angular/core';

import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';

import { User as IUserResponse, IUserVariables } from 'shared/models/user.model';

const USER_FRAGMENT = gql`
  fragment UserFragment on User {
    uuid
    firstName
    lastName
    email
    newsletter
    createdAt
    lastModifiedAt
  }
`;

const GET_USERS = gql`
  query {
      users {
        ...UserFragment
      }
  }
  ${USER_FRAGMENT}
`;

const CREATE_USER_MUTATION = gql`
  mutation createUser($variables: CreateUserInput!) {
    createUser(input: $variables) {
      ok
      error
      user {
        ...UserFragment
      }
    }
  }
  ${USER_FRAGMENT}
`;

const DELETE_USER_MUTATION = gql`
  mutation createUser($uuid: String!) {
    deleteUser(uuid: $uuid) {
      ok
    }
}`;


@Injectable()
export class UserService {

  constructor(private apollo: Apollo) { }

  get() {
    return this.apollo.query<IUserResponse>({
      query: GET_USERS
    });
  }

  create(user: IUserVariables) {
    return this.apollo.mutate<IUserVariables>({
      mutation: CREATE_USER_MUTATION,
      variables: {
        variables: {
          ...user
        }
      },
    });
  }

  delete(uuid: string) {
    return this.apollo.mutate({
      mutation: DELETE_USER_MUTATION,
      variables: {
        uuid
      }
    });
  }

  // PRIVATE //
}

