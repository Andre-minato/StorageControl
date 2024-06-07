import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import { useNavigate } from 'react-router-dom'
import './SaidaProduto.css'

const SaidaProduto = () => {

    const navigate = useNavigate()
    const { id } = useParams()
    const { descricao } = useParams()
    const { marca } = useParams()
    const { cor } = useParams()
    const { tamanho } = useParams()
    const { quantidade } = useParams()
  
    const [qtde_saida, setQtde_saida] = useState([])

    const produto_id = id

    const saidaProduto = async(e) => {
        e.preventDefault()

        if(Number(quantidade) >= qtde_saida){
          await blogFetch.post("/saidas", {
            produto_id,
            tamanho,
            cor,
            qtde_saida
          })
          navigate(`/produtos/${id}`)
          
          } else {
          
          alert("Quantidade de saída não pode ser maior que a quantidade em estoque!")
          navigate(`/produtos/${id}`)
      }
    }

      
      
      
  return (
    <div className='new-post'>
<h2>Saída de Produtos!</h2>
<form onSubmit={(e) => saidaProduto(e)}>
<div className="form-control">
  <label htmlFor="tamanho-produto"><h3>Descrição do Produto: </h3></label>
  <p><strong>Produto:</strong> ( {descricao} )</p>
  <p><strong>Marca:</strong> ( {marca} )</p>
  <p><strong>Cor:</strong> ( {cor} )</p>
  <p><strong>Tamanho:</strong> ( {tamanho} )</p>
</div>
<div className="form-control">
  <label htmlFor="quantidade-produto"><strong>Quantidade: </strong>{quantidade}</label>
  <input
    type="text"
    name='quantidade-produto'
    id='quantidade-produto'
    placeholder='Inserir quantidade do produto'
    onChange={(e) => setQtde_saida(e.target.value)}
  />
</div>
<input type="submit" value="Salvar" className='btn'/>
</form>
</div>
  )
}

export default SaidaProduto

