import { FaFire, FaPoo, FaHome } from "react-icons/fa";
import { MdOutlineSportsSoccer } from "react-icons/md";
import { SlGraph } from "react-icons/sl";
import { TbPlayFootball } from "react-icons/tb";




const SideBar = () => {
    return (
        <div className="fixed top-0 left-0 h-screen w-20 m-0 flex-none flex-col bg-gray-700 text-white shadow-lg z-50">
        <SideBarIcon icon={<MdOutlineSportsSoccer size="32"/>} text="Home"/>
        <SideBarIcon icon={<SlGraph size="32"/>} text="Stats"/>
        <SideBarIcon icon={<TbPlayFootball size="32"/>} text="Players"/>
    </div>
    );
}

const SideBarIcon = ({icon, text}) => {
    return (
        <div className="sidebar-icon group">
            {icon}
            <span className="sidebar-tooltip group-hover:scale-100">
                {text}
            </span>
        </div>
    );
}
export default SideBar;