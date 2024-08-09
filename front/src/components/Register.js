import React, { useState } from 'react';
import Input from './Input';
import Button from './Button';
import './Form.css'; // Reuse styles
import axios from 'axios';


const RegisterComponent = () => {
  const [name, setName] = useState('');
  const [username, setUsername] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);


  const handleRegister = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/register', {
        email,
        password,
      });
      console.log('Registration successful', response.data);
      // Handle successful registration (e.g., redirect to login, etc.)
    } catch (err) {
      console.error('Registration failed', err);
      setError('Registration failed. Please try again.');
    }
  };

  return (
    <div className="form-container">
      <h2>Register</h2>
      <form>
        <Input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          

        />
        <Input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          

        />
        <Input
          type="tel"
          placeholder="Phone"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          

        />
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
        <Button onClick={handleRegister} value={'Register'}/>
        {error && <p>{error}</p>}

      </form>
      <div className="forgot-password">
        <a href="/">Login</a>
      </div>
    </div>
  );
};

export default RegisterComponent;
