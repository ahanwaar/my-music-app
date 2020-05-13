import React from "react";
import { Route, Switch, Link } from "react-router-dom"
import "./App.css"
// import Apollo framework query hook
import { useQuery } from '@apollo/react-hooks'; // New
// import our queries previously defined
import { ARTIST_albums, ARTISTS_LIST_QUERY } from "./query" //New


const App = () => {
    return (
        <div className="App">
            <Switch>
                <Route exact path="/" component={MainPage} ></Route>
                <Route exact path="/artist/:slug" component={ArtistPage} ></Route>

            </Switch>
        </div>
    )
}

const MainPage = (props) => {
    const { loading, error, data } = useQuery(ARTISTS_LIST_QUERY);
    if (loading) return <div>Loading ...</div>
    if (error) return <div>Unexpected Error: {error.message}</div>
    return(
        <div className="root">
            {data && data.artists &&
                data.artists.map((artist) => (
                    <div className="artist-card" key={artist.slug} >
                        <Link to={`/artist/${artist.slug}`}>
                            <img
                            className="artist-card-image"
                            src={artist.artistPoster}
                            alt={artist.name}
                            title={artist.name}
                            />
                        </Link>
                    </div>
                ))
            }
        </div>
    )
}
function ArtistPage(props) {
     // uncomment to see which props are passed from router
    console.log(props)
    // due to we make slug parameter dynamic in route component,
    // urlParameters will look like this { slug: 'slug-of-the-selected-movie' }
    const urlParameters = props.match.params
    console.log(urlParameters)
    const { loading, error, data } = useQuery(ARTIST_albums , {
       variables:{slug:urlParameters.slug}});
    if (loading) return <div>Loading</div>
    if (error) return <div>Unexpected Error: {error.message}</div>

    return (
        <div className="root">
            {data && data.artist &&
                <div className="artist-card">
                    {data.artist.albums.map(album =>{
                        return(
                             <img
                        className="artist-card-image"
                        src={album.albumPoster}
                        alt={album.title }
                        title={album.title }
                    />
                            )
                    })}
                </div>
            }
        </div>
    )
}


export default App