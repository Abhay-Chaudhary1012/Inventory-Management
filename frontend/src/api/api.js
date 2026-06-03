import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: { "Content-Type": "application/json" }
});

export const productService = {
  getAll: () => apiClient.get("/products"),
  getById: (id) => apiClient.get(`/products/${id}`),
  create: (data) => apiClient.post("/products", data),
  update: (id, data) => apiClient.put(`/products/${id}`, data),
  remove: (id) => apiClient.delete(`/products/${id}`)
};

export const customerService = {
  getAll: () => apiClient.get("/customers"),
  getById: (id) => apiClient.get(`/customers/${id}`),
  create: (data) => apiClient.post("/customers", data),
  update: (id, data) => apiClient.put(`/customers/${id}`, data),
  remove: (id) => apiClient.delete(`/customers/${id}`)
};

export const orderService = {
  getAll: () => apiClient.get("/orders"),
  getById: (id) => apiClient.get(`/orders/${id}`),
  create: (data) => apiClient.post("/orders", data),
  remove: (id) => apiClient.delete(`/orders/${id}`)
};

export const dashboardService = {
  getStats: () => apiClient.get("/dashboard/stats")
};

export default apiClient;