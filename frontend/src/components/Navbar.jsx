import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar navbar-dark bg-dark navbar-expand-lg">
      <div className="container">
        <span className="navbar-brand">
          Inventory Management
        </span>

        <div className="navbar-nav">
          <Link className="nav-link" to="/">
            Products
          </Link>

          <Link className="nav-link" to="/customers">
            Customers
          </Link>

          <Link className="nav-link" to="/orders">
            Orders
          </Link>
        </div>
      </div>
    </nav>
  );
}