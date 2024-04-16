export type User = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
};

export type ChangePasswordData = {
  password: string;
  confirm_password: string;
};
