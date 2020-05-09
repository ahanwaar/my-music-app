import React, {Component} from 'react';
import './App.css';
import ArtistList from "./components/ArtistList";

class App extends Component {
    state ={
        artists :[],
        albums :[],
        songs: [],
    }

    componentDidMount() {
      //fetch data
      fetch('http://127.0.0.1:8000/api/artists/', {
          method: 'Get',
          headers: {
              'Authorization': 'Token 43edb57ff6508957c16bd0c5e8967eeae985527e'
          }
      }).then(resp => resp.json())
          .then(res => this.setState({artists: res}))
      .catch(error => console.log(error))
    }

    render() {
        return (
        <div className="App">
            <h1>Artist Lists :</h1>
            <div className="layout">
                <ArtistList artists={this.state.artists} albums={this.state.albums} />
            </div>
        </div>
        );
    }
}

export default App;
