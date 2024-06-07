import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import { useNavigate } from 'react-router-dom'
const CorTamanho = () => {

  const navigate = useNavigate()

  const {id} = useParams()
  const [tamanho, setTamanho] = useState([])
  const [cor, setCor] = useState([])
  const produto_id = id


  const inserirProduto = async(e) => {
      e.preventDefault()
    
      await blogFetch.post("/tamanho_cor", {
          tamanho,
          cor,
          produto_id
        })
        navigate(`/produtos/${id}`)
    }
        

  return (
    <div className='new-post'>
      <h2>Adicionar Tamanho e Cor:</h2>
      <form onSubmit={(e) => inserirProduto(e)}>
      <div className="form-control">
        <label htmlFor="tamanho-produto">Tamanho:</label>
        <input
          type="text"
          name='tamanho-produto'
          id='tamanho-produto'
          placeholder='Inserir tamanho do produto'
          onChange={(e) => setTamanho(e.target.value)}
        />
      </div>
      <div className="form-control">
        <label htmlFor="cor-produto">Cor:</label>
        <input
          type="text"
          name='cor-produto'
          id='cor-produto'
          placeholder='Inserir cor do produto'
          onChange={(e) => setCor(e.target.value)}
        />
      </div>
      <input type="submit" value="Cadastrar" className='btn'/>
      </form>
    </div>
  )
}

export default CorTamanho