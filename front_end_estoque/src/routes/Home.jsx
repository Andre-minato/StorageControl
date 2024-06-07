import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { Link } from "react-router-dom"
import "./Home.css"


const Home = () => {

  const [posts, setPost] = useState([])

  const getPosts = async() => {
    try {
      const response = await blogFetch.get("/produtos")
      const data = response.data
      setPost(data)
      console.log(data)
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getPosts()
  }, [])
  
  return (
    <div className='home'>
      <h1>Produtos</h1><br />
      {posts.length === 0 ? (<p>Não tem produto em estoque!</p>) : (
        posts.map((post) => (
          <div className="post" key={post.id}>
            <h3>Categoria: { post.categoria}</h3><br />
            <p><strong>Produto: </strong>{post.descricao}</p>
            <p><strong>Marca: </strong>{post.marca}</p><br />
            <ul>
              <li>
                <Link to={`/produtos/${post.id}`} className='new-btn' >
                  Detalhe Produto
                </Link><br />
              </li>
            </ul>
          </div>
        ))
      )}
    </div>
  )
}

export default Home



