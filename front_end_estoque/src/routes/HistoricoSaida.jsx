import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"

import "./HistoricoSaida.css"

const HistoricoSaida = () => {
    const { id } = useParams()

    const [saida, setSaida] = useState([])

    const getSaida = async() => {
      try {
        const response = await blogFetch.get(`/saidas/${id}`)                                       
        const data = await response.data
        setSaida(data)
        console.log(await data[0])
        
      } catch (error) {
        console.log(error)
      }
    }
  
    useEffect(() => {
      getSaida()
    }, [])


  return (
    <div className="container">
        <table>
        <thead>
            <h2>Histórico de Saída</h2><br />
            <tr>
                <th>Data de Saida</th>
                <th>Hora de Saida</th>
                <th>Tamanho</th>
                <th>Cor</th>
                <th>Quantidade</th>
                <th>id Produto</th>
            </tr>
        </thead>
        <tbody>
          {saida.map(item => (
            <tr key={item.id} className="item">
              <td>{item.data_entrada}</td>
              <td>{item.hora_entrada}</td>
              <td>{item.tamanho}</td>
              <td>{item.cor}</td>
              <td>{item.quantidade}</td>
              <td>{item.produto_id}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>  
  )
}

export default HistoricoSaida