import React, { useState } from 'react';
import Input from './Input';
import Button from './Button';
import './Form.css';
import axios from 'axios';

const FormComponent = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/login', {
        email,
        password,
      });
      console.log('Login successful', response.data);
      // Handle successful login (e.g., save the token, redirect, etc.)
    } catch (err) {
      console.error('Login failed', err);
      setError('Login failed. Please check your credentials.');
    }
  };

  return (
    <div className="form-container">
      <h2>Login</h2>
      <form onSubmit={(e) =>{
        e.preventDefault();
        handleLogin();
      }}>
        <Input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          
        />
        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          
        />
        <Button onClick={handleLogin} value={'Login'}/>
        {error && <p>{error}</p>}
        <div className="forgot-password">
          <a href="/register">Register</a>
        </div>
      </form>
    </div>
  );
};

export default FormComponent;
