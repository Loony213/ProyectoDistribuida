import React, { useState } from 'react';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const userData = { username, password };

    fetch('http://localhost:5001/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })
      .then(response => response.json())
      .then(data => {
        if (data.token) {
          alert('Inicio de sesión exitoso');
        } else {
          alert('Error al iniciar sesión');
        }
      })
      .catch(error => alert('Error en la conexión'));
  };

  return (
    <div>
      <h2>Iniciar sesión</h2>
      <form onSubmit={handleSubmit}>
        <label>Nombre de Usuario:</label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <br />
        <label>Contraseña:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <br />
        <button type="submit">Iniciar sesión</button>
      </form>
    </div>
  );
};

export default Login;
