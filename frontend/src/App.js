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
                <Route exact path="/artist/:slug" component={MoviePage} ></Route>
            </Switch>
        </div>
    )
}

const MainPage = (props) => {
    const { loading, error, data } = useQuery(ARTISTS_LIST_QUERY);
    if (loading) return <div>Loading</div>
    if (error) return <div>Unexpected Error: {error.message}</div>
    return(
        <div>
            {data && data.artists &&
                data.artists.map(artist => (
                    <div className="artist-card" key={artist.slug}>

                        <img
                            className="artist-card-image"
                            src={artist.artistPoster}
                            alt={artist.name + " poster"}
                            title={artist.name + " poster"}
                        />
                        <Link to={`/artist/${artist.slug}`} className="movie-card-link" />
                    </div>
                ))
            }
        </div>
    )
}

const MoviePage = (props) => {
    // uncomment to see which props are passed from router
    //console.log(props)
    // due to we make slug parameter dynamic in route component,
    // urlParameters will look like this { slug: 'slug-of-the-selected-movie' }
    const urlParameters = props.match.params
    const { loading, error, data } = useQuery(ARTIST_QUERY, {
        variables:{slug:urlParameters.slug}
    });
    if (loading) return <div>Loading</div>
    if (error) return <div>Unexpected Error: {error.message}</div>

    return (
        <div className="movie-page">
        <Link to="/" className="back-button" >Main Page</Link>
            {data && data.artist &&
                <div className="movie-page-box">
                    <img
                        className="movie-page-image"
                        src={data.artist.artistUrl}
                        alt={data.artist.name + " poster"}
                        title={data.artist.name + " poster"}
                    />
                    <div className="movie-page-info">
                        <h1>{data.artist.name}</h1>
                        <br />
                    </div>
                </div>
            }
        </div>
    )
}
export default App