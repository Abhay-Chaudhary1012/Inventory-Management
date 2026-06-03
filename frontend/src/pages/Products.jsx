import { useEffect, useState } from "react";
import api from "../api/api";
import ProductForm from "../components/ProductForm";

export default function Products() {
  const [products, setProducts] = useState([]);

  const loadProducts = async () => {
    try {
      const res = await api.get("/products");
      setProducts(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadProducts();
  }, []);

  return (
    <div className="container mt-4">
      <h2>Products</h2>

      <ProductForm />

      <div className="card mt-4">
        <div className="card-header">
          Product List
        </div>

        <div className="card-body">
          <button
            className="btn btn-secondary mb-3"
            onClick={loadProducts}
          >
            Refresh
          </button>

          <table className="table table-bordered">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>SKU</th>
                <th>Price</th>
                <th>Stock</th>
              </tr>
            </thead>

            <tbody>
              {products.length === 0 ? (
                <tr>
                  <td colSpan="5" className="text-center">
                    No Products Found
                  </td>
                </tr>
              ) : (
                products.map((product) => (
                  <tr key={product.id}>
                    <td>{product.id}</td>
                    <td>{product.name}</td>
                    <td>{product.sku}</td>
                    <td>{product.price}</td>
                    <td>{product.stock}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}