import React, { useEffect, useState } from 'react';
import resemble from 'resemblejs';
import '../styles/game.css'

const Game = () => {
  const [image1,setImage1] = useState()
  const [image2,setImage2] = useState()
  const [diff, setDiff] = useState()
  useEffect(() => {
    (async () => {
      try {
        
        const response = await fetch(import.meta.env.VITE_BACKEND_URL +`api/start_game`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        const result = await response.json();
        const img1 = new Image()
        img1.onload = () =>{
          setImage1(img1)
        }
        img1.src = result.og_url

        const img2 = new Image()
        img2.onload = () =>{
          setImage2(img2)
        }
        img2.src = result.diff_url

        setDiff(result.coors)


      } catch (error) {
        console.log("Error loading message from backend");
      }
    })();
  }, []);



  
  const click_registrator = (e) =>{
    const offsetX = e.target.offsetLeft;
    const offsetY = e.target.offsetTop;
    let xclick = (e.clientX - offsetX)
    let yclick = (e.clientY - offsetY)
    
    let coordinates = diff.filter(x => x.answered == false)
    
    for ( let i in coordinates){
      const distance = Math.sqrt(Math.pow(xclick - coordinates[i].coors[0], 2) + Math.pow(yclick - coordinates[i].coors[1], 2));
      if (distance <= 20){
        coordinates[i].answered = true
        console.log("yay")
        setDiff(coordinates)
      }

    }
    console.log(coordinates)
    
    
  }
 
  image1? console.log(image1.width):""

  return (
    <>
    <div className='row'>
      <div className='col-6'>{ image1? <img src={image1.src} className="img-fluid" alt="..." id ="img1"/> : <div className="spinner"></div>}</div>
      {image1 &&(<canvas id="myCanvas" 
          width={image1.width}
          height={image1.height}
          style={{ position: "absolute", top: image1.offsetTop, left: image1.offsetLeft, border: "1px solid red" }}></canvas>)}
      <div className='col-6'>{image2?<img src={image2.src} className="img-fluid" alt="..." onClick={e  => {click_registrator(e)}}/>:<div className="spinner"></div>}</div>
    </div>
    </>
  );
}

export default Game;
