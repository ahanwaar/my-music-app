import React  from "react";

function ArtistList(props){
    return(
        <div>
            {props.artists.map( artist => {
                return(<h4 key={artist.id} >{artist.name} </h4>); })}
         </div>
    )
}
export default ArtistList;