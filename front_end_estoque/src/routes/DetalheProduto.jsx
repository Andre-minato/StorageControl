import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import "./DetalheProduto.css"
import { Link } from "react-router-dom"

const DetalheProduto = () => {
  
  const btnEntrar = document.getElementById('btn-entrada')
  const { id } = useParams()
  const [posts, setPosts] = useState({})
  const getPost = async() => {
    try {
      const response = await blogFetch.get(`/produtos/${id}`)
      const data = response.data
      setPosts(data)
      console.log( await data[0].quantidade)
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getPost()
  }, [])
    
  return (
    <div className="post-container">
      <h1>estoque</h1>
      {!posts[0] ? (
        <p>Sem produto em estoque!</p>
      ) : ( 
      <div className="post">
        <p><strong>Produto: </strong>{posts[0].descricao}</p>
        <p><strong>Marca: </strong>{posts[0].marca}</p><br />
        <div className="btn-tamanho-cor">
          <ul>
            
            <li>
            <Link to={`/cor_tamanho/${id}`} className="btn-entrada" id="btn-tamanho-cor">Adicionar tamanho e cor</Link>
            </li>
            <li>
              <Link to={`/entradas/${id}`} className='btn-entrada' id="btn-entrada" >historico entrada</Link>
            </li>
            {/* <li>
              <Link to={`/saidas/${id}`} className="btn-entrada" id="btn-saida">historico de saída</Link> 
            </li> */}
          </ul>
        </div><br />
        <table>
          
        <thead>
            {/* <h3>Estoque do produto</h3> */}
            <tr>
                <th>Produto</th>
                <th>Marca</th>
                <th>Tamanho</th>
                <th>Cor</th>
                <th>Quantidade</th>
                <th>Opções</th>
            </tr>
        </thead>
        <tbody>
          {posts.map(item => (
            <tr key={item.id} className="item">
              <td>{item.descricao}</td>
              <td>{item.marca}</td>
              <td>{item.tamanho}</td>
              <td>{item.cor}</td>
              <td>{item.quantidade}</td>
              
              <td>
                {item.quantidade == null || item.quantidade == 0 ?(
                   null
                  ) : 
                    <Link to={`/saida_produto/${item.id}/${item.descricao}/${item.marca}/${item.cor}/${item.tamanho}/${item.quantidade}`} 
                    className="btn-saida" 
                    id="btn-saida"
                    >
                      Saída
                    </Link>
                  }
                {item.cor != null ? (
                  <Link to={`/entrada_produto/${item.id}/${item.descricao}/${item.marca}/${item.cor}/${item.tamanho}` } 
                  className="btn-entrada" 
                  >
                    entrada
                  </Link>
                ) : null}
                
              </td>
            </tr>
          ))}
        </tbody>
        </table> 
      </div>
      )}
    </div>
  )
}

export default DetalheProduto

