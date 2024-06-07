import { Link } from 'react-router-dom'

import './Navbar.css'
const Navbar = () => {
  return (
    <nav className="navbar">
        <h2>
        <Link to={`/`} className='btn-home'>Home</Link>
        </h2>
        <ul>
            <li>
                <Link to={`/nova_categoria`} className='new-btn'>Nova Categoria</Link>
            </li>
            <li>
                <Link to={`/categorias`} className='new-btn'>Novo Produto</Link>
            </li>
        </ul>
    </nav>
  )
}

export default Navbar