import React, { useEffect, useRef, useState } from 'react';
import resemble from 'resemblejs';
import '../styles/game.css'

const Game = () => {
  const [image1,setImage1] = useState()
  const [image2,setImage2] = useState()
  const [diff, setDiff] = useState()
  const imageRef = useRef(null);
  const canvasRef = useRef(null)
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
        setDiff(result.coors)

        const img1 = new Image()
        setImage1(img1)
        img1.src = result.og_url

        const img2 = new Image()
        setImage2(img2)
        img2.src = result.diff_url
        
        if (canvasRef.current &&imageRef.current) {
          const imageRect = imageRef.current.getBoundingClientRect();
          const canvas = canvasRef.current.getBoundingClientRect();

          console.log('Image Coordinates:', {
            top: imageRect.top,
            left: imageRect.left,
            right: imageRect.right,
            bottom: imageRect.bottom,
            width: imageRect.width,
            height: imageRect.height,
          });

          console.log('canvas Coordinates:', {
            top: canvas.top,
            left: canvas.left,
            right: canvas.right,
            bottom: canvas.bottom,
            width: canvas.width,
            height: canvas.height,
          });
        }
        
        if(canvasRef.current && imageRef.current){
          
          const imageRect = imageRef.current.getBoundingClientRect();
          const canvas = canvasRef.current;

          canvas.width = imageRect.width;
          canvas.height = imageRect.height;

          canvas.style.position = "absolute";
          
          canvas.style.top = `${imageRect.top}px`;
          canvas.style.left = `${imageRect.left}px`;

          

        }
        
        

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

  const drawCircle = (x, y) => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    ctx.beginPath();
    ctx.arc(x, y, 10, 0, Math.PI * 2); // Change the radius (20) as needed
    ctx.fillStyle = 'blue'; // Change the fill color as needed
    ctx.fill();
    ctx.closePath();
  };

  const handleClick = (event) => {
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;

    // Call the drawCircle function with the click coordinates
    drawCircle(mouseX, mouseY);
  };
  
  
  

  return (
    <>
    <div className='row   border' style={{ margin: 0, padding: 0 }}>
      <div className='col-6 ' style={{ margin: 0, padding: 0 }}>{image1 &&(
        <img src={image1.src} className="img-fluid" alt="..." ref={imageRef} />
      )}
      <canvas id="canvas1" ref={canvasRef} style={{ border: "1px solid red", position: "absolute", }} onClick={handleClick}></canvas>
      </div>
      
      
    </div>
    </>
  );
}

export default Game;
