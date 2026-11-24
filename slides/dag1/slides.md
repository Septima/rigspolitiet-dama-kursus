---
marp: true
paginate: true
style: |

  section::after {
    color: white;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 3rem;

  }

  .center {
    text-align: center;
  }

  .topbar {
  padding-top: 125px;
  }

    .top50 {
  padding-top: 50px;
  }

      .top100 {
  padding-top: 100px;
  }

        .top150 {
  padding-top: 150px;
  }
  img{background-color:transparent}

  header {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 1fr 1fr;
        grid-gap: 10px;
        box-sizing: border-box;
        justify-content: center;
        width: 100%;
    }

    header img {
        height: 50px;
    }

  footer {
        display: grid;
        grid-template-columns: 1fr max-content;
        #background-color: #bb2e29;
        color: white;
        align-content: right;
        font-size: 20px;
    }

  h1 {
  font-size: 70px;
  color: white;
    }  
  h2 {
  font-size: 50px;
  color: white;
    }

  h3 {
  font-size: 30px;
  color: white;
    }
    
  .slide_heaader {
    position:absolute;top:90px;left:75px;right:75px;font-size:50px;

  }

  li::marker {
  color: #397c67;
    }

   li {
  color: white;
  padding: 0px;
  font-size:30px;
  }

   p {
  color: white;
  padding: 0px;
  padding-top: 30px;
  font-size:30px;
  }

  img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }

      .container {
    display: flex;
  }
  .col {
    flex:1;
    padding-right: 20px;
    padding-left: 20px;
    padding-top: 120px;

  }
    .col_tight {
    flex:1;
    padding-right: 20px;
    padding-left: 20px;
    padding-top: 60px;

  }

  .center_img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  }

header:  ![alt text](../../ressources/logo/septima.svg "Title")

footer: Python-scripting i QGIS med PyQGIS  





        
---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:200px;left:75px;right:75px;font-size:70px;">Python-scripting i QGIS med PyQGIS.</h1>
<h2 style="position:absolute;top:360px;left:75px;right:75px;font-size:45;">Morten Fuglsang</h2>
<h3 style="position:absolute;top:430px;left:75px;right:75px;font-size:30;">12.05.2026</h3>


--- 