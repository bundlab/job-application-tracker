import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor (add token later)
api.interceptors.request.use(config => {
  return config;
});

// Response interceptor (handle 401, etc.)
api.interceptors.response.use(
  response => response,
  error => {
    // handle global errors here
    return Promise.reject(error);
  }
);

export default api;
