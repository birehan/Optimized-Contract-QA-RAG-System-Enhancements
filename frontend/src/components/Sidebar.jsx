import CreateChat from './CreateChat'
import {Link} from 'react-router-dom'
const Sidebar = ({setIsContractCreated}) => {
  return (
    <div className="bg-[#f0f4f9] text-black w-64 p-4 space-y-4">
  <Link to="/">
  <div className="text-xl font-semibold mb-16">LizzyAI</div>
  </Link>
   <CreateChat setIsContractCreated={setIsContractCreated}/>
    <div className="pt-2" >
      <div className="text-gray-700 text-sm">History</div>

      <ul className="space-y-2 mt-3">
        <li></li>
        <li></li>
        {/* <!-- More conversations --> */}
      </ul>
    </div>
  </div>
  )
}

export default Sidebar