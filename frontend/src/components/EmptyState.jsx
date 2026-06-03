import { LuInbox } from "react-icons/lu";

export default function EmptyState({ title, message, icon: Icon = LuInbox }) {
  return (
    <div className="empty-state">
      <Icon size={48} className="empty-icon" />
      <h3 className="empty-title">{title || "No records found"}</h3>
      {message && <p className="empty-message">{message}</p>}
    </div>
  );
}
