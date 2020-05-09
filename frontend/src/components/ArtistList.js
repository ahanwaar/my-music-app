import React  from "react";

function ArtistList() {
    const  artists = ['Sia', 'Marina'];

    return(
        <React.Fragment>
            { artists.map( artist => {
                return <h3>{artist}</h3>
            })}
         </React.Fragment>
    )
}

export default ArtistList;