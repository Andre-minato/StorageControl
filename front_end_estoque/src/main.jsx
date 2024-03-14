import Home from './routes/Home.jsx'
import NovoProduto from './routes/NovoProduto.jsx'
import Categoria from './routes/Categoria.jsx'
import HistoricoEntrada from './routes/HistoricoEntrada.jsx'
import NovaCategoria from './routes/NovaCategoria.jsx'
import DetalheProduto from './routes/DetalheProduto.jsx'
import EntradaProduto from './routes/EntradaProduto.jsx'
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { createBrowserRouter, RouterProvider, Route } from 'react-router-dom'
import './index.css'

const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: "/",
        element: <Home />
      },
      {
        path: "/new/:id",
        element: <NovoProduto />
      },
      {
        path: "/produtos/:id",
        element: <DetalheProduto />
      },
      {
        path: "/categorias",
        element: <Categoria />
      },
      {
        path: "/entradas/:id",
        element: <HistoricoEntrada />
      }, 
      {
        path: "nova_categoria",
        element: <NovaCategoria />
      },
      {
        path: "/entrada_produto/:id",
        element: <EntradaProduto />
      }
    ]
  }
])



ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
