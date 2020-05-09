import React  from "react";

function ArtistList(props) {
    return (
        <div>
            {props.artists.map(artist => {
                return (
                    <ul key={artist.id}>
                        <h3>{artist.name}</h3>
                        <li>Albums:</li>
                        <ul>
                            {artist.albums.map(album => {
                                return (
                                    <ul>
                                        <li>{album.title}</li>
                                        <ul>
                                            <li>{album.year}</li>

                                            {album.songs.map(song => {
                                                return (
                                                    <ul>
                                                        <li>{song.title}</li>
                                                    </ul>
                                                )
                                            })}
                                        </ul>

                                    </ul>

                                );
                            })}

                        </ul>
                        <hr color="white"/>
                    </ul>


                );
            })}
        </div>
    )
}

export default ArtistList;