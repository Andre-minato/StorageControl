import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import "./DetalheProduto.css"
import { Link } from "react-router-dom"

const DetalheProduto = () => {
  const { id } = useParams()
  const [posts, setPosts] = useState({})
  const getPost = async() => {
    try {
      const response = await blogFetch.get(`/produtos/${id}`)
      const data = response.data
      setPosts(data)
      console.log( await data[0])
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getPost()
  }, [])
  
  return (
    <div className="post-container">
      {!posts[0] ? (
        <p>Sem produto em estoque!</p>
      ) : ( 
      <div className="post">
        <h3>Produto: {posts[0].categoria}</h3><br />
        <p><strong>Marca: </strong>{posts[0].marca}</p>
        <p><strong>Descrição: </strong>{posts[0].descricao}</p><br />
        
        <table>
        <thead>
            <h2>Estoque do produto</h2>
            {/* <select>
              <option>COR</option>
              {posts.map(cor => (
                <option value={cor.cor}>{cor.cor}</option>
              ))}
            </select> */}
            <tr>
                <th>Categoria</th>
                <th>Tamanho</th>
                <th>Marca</th>
                <th>Descrição</th>
                <th>Cor</th>
                <th>Quantidade</th>
            </tr>
        </thead>
        <tbody>
          {posts.map(item => (
            <tr key={item.id} className="item">
              <td>{item.categoria}</td>
              <td>{item.tamanho}</td>
              <td>{item.marca}</td>
              <td>{item.descricao}</td>
              <td>{item.cor}</td>
              <td>{item.quantidade}</td>
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