export interface IUserVariables {
    email: string;
    firstName: string;
    lastName: string;
    newsletter: boolean;
}

export interface User extends IUserVariables {
  uuid: string;
  createdAt: Date;
  lastModifiedAt: Date | null;
}

export enum UserErrors {
  INVALID_EMAIL = "Invalid email submitted",
  ALREADY_CREATED = "This email has already been used"
}
