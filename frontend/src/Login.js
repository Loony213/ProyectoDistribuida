import React, { useState } from 'react';

const DeleteUser = () => {
  const [userId, setUserId] = useState('');

  const handleDelete = () => {
    fetch(`http://localhost:5000/api/delete/${userId}`, {
      method: 'DELETE',
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message) {
          alert('Usuario eliminado exitosamente');
        } else {
          alert('Error al eliminar el usuario');
        }
      })
      .catch((error) => alert('Error en la conexión'));
  };

  return (
    <div>
      <h2>Eliminar Usuario</h2>
      <input
        type="number"
        placeholder="ID del usuario"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        required
      />
      <button onClick={handleDelete}>Eliminar Usuario</button>
    </div>
  );
};

export default DeleteUser;
