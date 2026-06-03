import { useState } from "react";

export default function ProductForm() {
  const [form, setForm] = useState({
    name: "",
    sku: "",
    price: "",
    stock: ""
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log("Product Data:", form);

    setForm({
      name: "",
      sku: "",
      price: "",
      stock: ""
    });
  };

  return (
    <div className="card p-3 mt-3">
      <h4>Add Product</h4>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <input
            className="form-control"
            placeholder="Product Name"
            name="name"
            value={form.name}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <input
            className="form-control"
            placeholder="SKU"
            name="sku"
            value={form.sku}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <input
            className="form-control"
            placeholder="Price"
            name="price"
            type="number"
            value={form.price}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <input
            className="form-control"
            placeholder="Stock"
            name="stock"
            type="number"
            value={form.stock}
            onChange={handleChange}
          />
        </div>

        <button className="btn btn-primary" type="submit">
          Save Product
        </button>
      </form>
    </div>
  );
}