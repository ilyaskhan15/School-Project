import { useState } from "react";
import api from "../api/axios";

const Register = () => {
  const [form, setForm] = useState({
    email: "",
    username: "",
    password: "",
    first_name: "",
    last_name: "",
    phone_number: "",
    date_of_birth: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/auth/register/", form);
      alert("Registration successful");
    } catch (err) {
      alert(JSON.stringify(err.response?.data));
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>

      <input name="email" placeholder="Email" onChange={handleChange} />
      <input name="username" placeholder="Username" onChange={handleChange} />
      <input type="password" name="password" placeholder="Password" onChange={handleChange} />
      <input name="first_name" placeholder="First Name" onChange={handleChange} />
      <input name="last_name" placeholder="Last Name" onChange={handleChange} />
      <input name="phone_number" placeholder="Phone" onChange={handleChange} />
      <input type="date" name="date_of_birth" onChange={handleChange} />

      <button type="submit">Register</button>
    </form>
  );
};

export default Register;
