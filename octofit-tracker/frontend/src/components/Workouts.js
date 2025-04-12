import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://glorious-happiness-wp6r7v4vw7435vw6-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div>
      <h1 className="display-4">Workouts</h1>
      <button className="btn btn-primary mb-3" onClick={() => alert('Add Workout clicked!')}>Add Workout</button>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout, index) => (
            <tr key={index}>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
              <td>
                <button className="btn btn-danger" onClick={() => alert('Delete Workout clicked!')}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;
