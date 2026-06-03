import { LuPlus } from "react-icons/lu";

export default function PageHeader({ title, subtitle, actionLabel, onAction }) {
  return (
    <div className="page-header">
      <div>
        <h1 className="page-title">{title}</h1>
        {subtitle && <p className="page-subtitle">{subtitle}</p>}
      </div>

      {actionLabel && (
        <button className="btn btn-primary" onClick={onAction}>
          <LuPlus size={18} />
          {actionLabel}
        </button>
      )}
    </div>
  );
}
