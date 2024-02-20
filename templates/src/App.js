import React, { useState, useEffect } from 'react';

function App() {
  const [plateDetects, setPlateDetects] = useState([]);
  const [latestPlate, setLatestPlate] = useState("");

  useEffect(() => {
    // Fungsi untuk mengambil data dari API
    const fetchData = () => {
      fetch('http://localhost:1500/platedetect')
        .then(response => response.json())
        .then(data => {
          // Mengurutkan data berdasarkan tanggal dan waktu
          const sortedData = data.data.sort((a, b) => new Date(b.date) - new Date(a.date));
          setPlateDetects(sortedData);
          // Mengambil nomor plat dari data teratas (data terbaru)
          if (sortedData.length > 0) {
            setLatestPlate(sortedData[0].number_plate);
          }
        })
        .catch(error => console.error('Error fetching data:', error));
    };

    // Panggil fetchData setiap 5 detik
    const intervalId = setInterval(fetchData, 1000);

    // Bersihkan interval saat komponen tidak lagi digunakan
    return () => clearInterval(intervalId);
  }, []); // Kondisi dependency kosong agar hanya dijalankan sekali saat komponen dipasang

  return (
    <div>
      <h1>Data Plate Detect</h1>
      <div style={{ display: "flex" }}>
        <div style={{ marginRight: "20px" }}>
          <h2>Plat Nomor Terbaru</h2>
          <p>{latestPlate}</p>
        </div>
        <div>
          <a href="http://127.0.0.1:5000/opencam" rel="noopener noreferrer">
            <button>Open Camera</button>
          </a>
          <table>
            <thead>
              <tr>
                <th>No. Plat</th>
                <th>Tanggal</th>
              </tr>
            </thead>
            <tbody>
              {plateDetects.map((plateDetect, index) => (
                <tr key={index}>
                  <td>{plateDetect.number_plate}</td>
                  <td>{plateDetect.date}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default App;
