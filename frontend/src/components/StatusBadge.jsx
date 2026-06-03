export default function StatusBadge({ stock }) {
  if (stock <= 0) {
    return <span className="badge badge-danger">Out of Stock</span>;
  }
  if (stock < 10) {
    return <span className="badge badge-warning">Low Stock</span>;
  }
  return <span className="badge badge-success">In Stock</span>;
}
