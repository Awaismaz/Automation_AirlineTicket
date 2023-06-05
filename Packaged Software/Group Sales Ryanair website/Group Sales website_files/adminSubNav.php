

<style type=”text/css”>
    /*Initialize*/
    ul#menuAdminSubNav, ul#menuAdminSubNav ul.sub-menuAdminSubNav {
        padding:0;
        margin: 0;
    }
    ul#menuAdminSubNav li, ul#menuAdminSubNav ul.sub-menuAdminSubNav li {
        list-style-type: none;
        display: inline-block;
    }
    /*Link Appearance*/
    ul#menuAdminSubNav li a, ul#menuAdminSubNav li ul.sub-menuAdminSubNav li a {
        text-decoration: none;
        color: #5a5a5a;
        /* background: #F7F7F7;*/
        padding: 4px 5px 2px 4px;
        display:inline-block;
    }
    /*Make the parent of sub-menuAdminSubNav relative*/
    ul#menuAdminSubNav li {
        position: relative;
    }
    /*sub menuAdminSubNav*/
    ul#menuAdminSubNav li ul.sub-menuAdminSubNav {
        display:none;
        position: absolute;
        top: 19px;
        left: 0px;
        width: 150px;
        background-color:#FFFFFF;
        padding: 4px 5px 4px 4px;
        text-align:left;
        border: 1px solid #aeaeae;

    }
    ul#menuAdminSubNav li:hover ul.sub-menuAdminSubNav {
        display:block;
        background-color:#none;
    }




    ul#menuAdminSubNav li a.current, ul#menuAdminSubNav li a.current:visited {
        color:#ff9933;
        text-decoration:none;
        font-size:11px;
        letter-spacing:-0.5px;
        letter-spacing:-0.5px;
        background-color:#fff;
        padding:4px 5px 2px 4px;
        font-weight:bold;
    }
    ul#menuAdminSubNav li a.current:hover {
        color:#ff9933;
        text-decoration:none;
        background-color:#eeeeee;
        font-size:11px;
        letter-spacing:-0.5px;
        letter-spacing:-0.5px;
    }

</style>
