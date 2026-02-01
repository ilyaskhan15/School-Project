import { logout } from "../utils/auth";

const Dashboard = () => {
  return (
    <div>
      <h2>Dashboard</h2>
      <button onClick={logout}>Logout</button>
    </div>
  );
};

export default Dashboard;
