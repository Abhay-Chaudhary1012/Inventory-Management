import { NavLink } from "react-router-dom";
import {
  LuLayoutDashboard,
  LuPackage,
  LuUsers,
  LuShoppingCart,
  LuX
} from "react-icons/lu";

const navItems = [
  { path: "/", label: "Dashboard", icon: LuLayoutDashboard },
  { path: "/products", label: "Products", icon: LuPackage },
  { path: "/customers", label: "Customers", icon: LuUsers },
  { path: "/orders", label: "Orders", icon: LuShoppingCart },
];

export default function Sidebar({ isOpen, onClose }) {
  return (
    <>
      {isOpen && (
        <div className="sidebar-overlay" onClick={onClose} />
      )}

      <aside className={`sidebar ${isOpen ? "sidebar--open" : ""}`}>
        <div className="sidebar-brand">
          <LuPackage size={22} />
          <span>Inventory Manager</span>
        </div>

        <nav className="sidebar-nav">
          {navItems.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              end={item.path === "/"}
              className={({ isActive }) =>
                `sidebar-link ${isActive ? "active" : ""}`
              }
              onClick={onClose}
            >
              <item.icon size={19} className="sidebar-link-icon" />
              <span>{item.label}</span>
            </NavLink>
          ))}
        </nav>

        <button className="sidebar-close" onClick={onClose}>
          <LuX size={18} />
        </button>
      </aside>
    </>
  );
}
