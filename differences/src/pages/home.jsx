import React from "react";
import { useNavigate } from "react-router-dom";

const Home = () =>{
    const navigate = useNavigate()

    
    return(
        <>
            
            <button className="btn btn-primary" onClick={() => {navigate('/differences', { replace: true })}}>start</button>
        </>
    )
}


export default Home