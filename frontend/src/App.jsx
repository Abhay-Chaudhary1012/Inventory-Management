import { useEffect, useState } from "react";
import api from "./api/api";

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    const res = await api.get("/products");
    setProducts(res.data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Inventory Management</h1>

      <button onClick={loadProducts}>
        Refresh Products
      </button>

      <hr />

      {products.map((p) => (
        <div key={p.id}>
          <h3>{p.name}</h3>
          <p>SKU: {p.sku}</p>
          <p>Price: {p.price}</p>
          <p>Stock: {p.stock}</p>
        </div>
      ))}
    </div>
  );
}

export default App;