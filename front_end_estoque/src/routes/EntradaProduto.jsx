import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import { useNavigate } from 'react-router-dom'


import "./EntradaProduto.css"


const EntradaProduto = () => {

  const navigate = useNavigate()

  const {id} = useParams()
  const {descricao} = useParams()
  const {marca} = useParams()
  const {cor} = useParams()
  const {tamanho} = useParams()
  const [qtde_entrada, setQtde_entrada] = useState([])
  const produto_id = id

  
  

  const inserirProduto = async(e) => {
      e.preventDefault()
      await blogFetch.put("/entradas", {
        tamanho,
        qtde_entrada,
        cor,
        produto_id
      })
      navigate(`/produtos/${id}`)
       
    }


  return (
    <div className='new-post'>
      <h2>Entrada de Produtos!</h2>
      <form onSubmit={(e) => inserirProduto(e)}>
      <div className="form-control">
        <label htmlFor="tamanho-produto"><h3>Descrição do Produto: </h3></label>
        <p><strong>Produto:</strong> ( {descricao} )</p>
        <p><strong>Marca:</strong> ( {marca} )</p>
        <p><strong>Cor:</strong> ( {cor} )</p>
        <p><strong>Tamanho:</strong> ( {tamanho} )</p>
      </div>
      <div className="form-control">
        <label htmlFor="quantidade-produto">Quantidade:</label>
        <input
          type="text"
          name='quantidade-produto'
          id='quantidade-produto'
          placeholder='Inserir quantidade do produto'
          onChange={(e) => setQtde_entrada(e.target.value)}
        />
      </div>
      <input type="submit" value="Salvar" className='btn'/>
      </form>
    </div>
  )
}


export default EntradaProduto
