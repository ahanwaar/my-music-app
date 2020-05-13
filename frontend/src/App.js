import React from "react";
import { Route, Switch, Link } from "react-router-dom"
import "./App.css"
// import Apollo framework query hook
import { useQuery } from '@apollo/react-hooks'; // New
// import our queries previously defined
import { ARTIST_QUERY, ARTISTS_LIST_QUERY } from "./query" //New

const App = () => {
    return (
        <div className="App">
            <Switch>
                <Route exact path="/" component={MainPage} ></Route>
            </Switch>
        </div>
    )
}

const MainPage = (props) => {
    const { loading, error, data } = useQuery(ARTISTS_LIST_QUERY);
    if (loading) return <div>Loading</div>
    if (error) return <div>Unexpected Error: {error.message}</div>
    return(
        <div className="root">
            {data && data.artists &&
                data.artists.map((artist) => (
                    <div className="artist-card" key={artist.id}>
                        <a href="#link">
                            <img
                            className="artist-card-image"
                            src={artist.artistPoster}
                            alt={artist.name}
                            title={artist.name}
                        />

                        </a>

                    </div>
                ))
            }
        </div>
    )
}


export default App