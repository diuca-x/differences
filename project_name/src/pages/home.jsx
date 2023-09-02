import React from "react";

const Home = () =>{

    const handleClieck = () =>{
        alert("agus pete")
    }
    return(
        <>
            
            <button class="btn btn-primary" onClick={() =>{handleClieck()}}>start</button>
        </>
    )
}


export default Home