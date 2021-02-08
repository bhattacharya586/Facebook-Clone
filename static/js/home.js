

$("#search__input").click(function(e) {
    console.log("2");
    var back = `
                <div onclick="back();" class="profile__msg">
                    <span><i class="fa fa-arrow-left"></i></span>    
                </div>
            `;
    document.getElementById("text__logo").innerHTML = back;
});



function addFriend(towhom){
    // Toast Up
    console.log("4");
    $(function() {
        $.ajax({
            url: '/friendsapi/'+towhom,
            success: function(data) {
                addfrnd = Object(data);
                if(addfrnd["status"]===1){
                    document.getElementById("toast__text").innerHTML = "Friend Request Sent Successfully"; 
                    $('#toast').show();
                    setTimeout(function(){
                        $('#toast').hide();
                    }, 5000);
                    $("#addId-"+towhom).prop("onclick", null).off("click");
                    document.getElementById("addId-"+towhom).innerHTML = 'Sent';
                    document.getElementById("addId-"+towhom).style.color = ' rgb(63, 197, 22)';
                }
                else if(addfrnd["status"]===2){
                    document.getElementById("toast__text").innerHTML = "You already have request pending"; 
                    $('#toast').show();
                    setTimeout(function(){
                        $('#toast').hide();
                    }, 5000);
                    
                }
                else{
                    document.getElementById("toast__text").innerHTML = "Something went wrong!!!"; 
                    $('#toast').show();
                    setTimeout(function(){
                        $('#toast').hide();
                    }, 5000);
                }
            }
        })
    });        
}

function search(){
    console.log("5");
    var val = document.getElementById("search__input").value;
    $(function() {
        $.ajax({
            url: '/api/'+val,
            success: function(data) {
                objet = Object(data);
                var content = "";
                for (let i = 0; i < objet["friends"].length; i++) {
                    if(objet["friends"][i][0]!=="{{user[0]}}")
                        content += `
                            <div class="left__bar__item">
                                <div class="left__bar__item">
                                    <img src="`+objet["friends"][i][3]+`" class="post__image__01__02" />
                                    <h6>`+objet["friends"][i][1].split(" ")[0]+` `+objet["friends"][i][1].split(" ")[1][0]+`.</h6>    
                                </div>
                                `;
                                console.log(objet["friends"][i]);
                        if(objet["friends"][i][4]==="New"){
                            content+=`<h6 id="addId-`+objet["friends"][i][0]+`" onclick="addFriend('`+objet["friends"][i][0]+`');" style="padding-top:5px !important;color:royalblue;"><i class="fa fa-user-plus"></i></h6>`;
                        }
                        else{
                            content+=`<h6 id="addId-`+objet["friends"][i][0]+`" style="padding-top:5px !important;color:rgb(63, 197, 22);">`+objet["friends"][i][4]+`</h6>`;
                        }
                                content+=`
                            </div>
                            <br>
                        `;
                }
                if(content.length==0)
                    document.getElementById("left__bar").innerHTML = "No user found";
                else
                    document.getElementById("left__bar").innerHTML = content;
            }
        });
    });
}

function triggerSignIn(id) {
    console.log("6");
    document.getElementById(id).style.display = "block";
    document.querySelector(".left").style.filter = "blur(4px)";
    document.querySelector(".middle").style.filter = "blur(4px)";
    document.querySelector(".right").style.filter = "blur(4px)";
    document.querySelector(".header__logo__search").style.filter = "blur(4px)";
    document.querySelector(".header__links").style.filter = "blur(4px)";
    document.querySelector(".profile__notification").style.filter = "blur(4px)";
    document.querySelector(".profile__msg").style.filter = "blur(4px)";
    document.querySelector(".message").style.filter = "blur(4px)";
}

$(".website").mouseup(function(e) {   
    console.log("7");
    document.getElementById("sign__in__register__02").style.display = "none";
    
    document.getElementById("sign__in__register").style.display = "none";
    if (($(e.target).closest(".left").length === 0 )||
            ($(e.target).closest(".middle").length === 0)||
            ($(e.target).closest(".right").length === 0)||
            ($(e.target).closest(".header__logo__search").length === 0)||
            ($(e.target).closest(".header__links").length === 0)||
            ($(e.target).closest(".profile__notification").length === 0)||
            ($(e.target).closest(".profile__msg").length === 0)||
            ($(e.target).closest(".message").length === 0)
        ) {
        $(".left").css("filter","none"); 
        $(".middle").css("filter","none"); 
        $(".right").css("filter","none"); 
        $(".profile__notification").css("filter","none"); 
        $(".header__logo__search").css("filter","none"); 
        $(".profile__msg").css("filter","none"); 
        $(".header__links").css("filter","none"); 
        $(".message").css("filter","none"); 
    }			 
});



function requestsFriends(type_,id) {
    $(function() {
        $.ajax({
            url: '/request/'+type_+'/'+id,
            success: function(data) {
                var stats = Object(data);
                console.log(stats);
                if(stats["status"]==="success"){
                    //    Get other friend requests
                    if(type_==="accept"){
                        $(function() {
                    $.ajax({
                        url: '/timeline',
                        success: function(data) {
                            var stats = Object(data);
                            var timeline = "";
                            for (let i = 0; i < stats["timeline"].length; i++) {
                                timeline += `
                                    <div class="post">
                                        <div class="post__heading">
                                            <div class="post__sender">
                                                <img src="`+stats["timeline"][i][24]+`" class="post__image__01" />
                                                <div class="names__post">
                                                    <h5>`+stats["timeline"][i][23]+`</h5>
                                                    <h6>`+stats["timeline"][i][16]+` : `+stats["timeline"][i][17]+` . <i class="fa fa-globe"></i></h6>
                                                </div>
                                            </div>
                                            <div class="post__options">
                                                <span><i class="fa fa-ellipsis-h"></i></span>
                                            </div>
                                        </div>
                                        <hr>
                                        <br>
                                        <div class="post__text__content">
                                            <p>`+stats["timeline"][i][15]+`</p>
                                        </div>
                                            <div class="row"><div class="row_posters post__image__content">
                                        `;

                                if(stats["timeline"][i][2]==="True"){
                                    for (let j = 0; j < stats["timeline"][i][9].split(",").length; j++) {
                                        timeline += `
                                                <img src="`+stats["timeline"][i][9].split(",")[j]+`" class="row_poster post__image__02" />
                                        `;    
                                    }  
                                }
                                timeline += "</div></div>"+`<div class="row"><div class="row_posters post__image__content">`;

                                if(stats["timeline"][i][3]==="True"){
                                    for (let j = 0; j < stats["timeline"][i][9].split(",").length; j++) {
                                        timeline += `
                                                <video class="post__image__02 row_poster" controls>
                                                    <source src="`+stats["timeline"][i][10].split(",")[j]+`" type="video/mp4">
                                                    <source src="`+stats["timeline"][i][10].split(",")[j]+`" type="video/ogg">
                                                    Your browser does not support the video tag.
                                                </video>
                                        `;    
                                    }  
                                }
                                timeline += "</div></div>";

                                timeline += `<div class="post__analytics">
                                            <div class="like__emoj">
                                                <p><span style="color: crimson;">❤</span>
                                                <span style="color: royalblue">👍</span>
                                                    <span style="color: yellow;">😢</span> 12K</p>
                                            </div>
                                            <div class="comment__share">
                                                <p>147 comments 72 shares</p>
                                            </div>
                                        </div>
                                        <br>
                                        <hr>
                                        <div class="post__footer">
                                            <div class="post__foot__item">
                                                <h3 class="icon__post__btn"><i class="fa fa-thumbs-up"></i></h3>
                                                <h3>Like</h3>
                                            </div>
                                            <div class="post__foot__item">
                                                <h3 class="icon__post__btn"><i class="fa fa-comment"></i></h3>
                                                <h3>Message</h3>
                                            </div>
                                            <div class="post__foot__item">
                                                <h3 class="icon__post__btn"><i class="fa fa-share"></i></h3>
                                                <h3>Share</h3>
                                            </div>
                                        </div>
                                        <div class="comment-section">
                                            <form>
                                                <input style="text-align: center;background: #292a2e63;border: none;outline:none;width:100%;padding-top: 20px;padding-bottom: 20px;color: white;font-size: 17px;" type="text" class="comment__Box" placeholder="Enter your comment here" />
                                            </form>
                                            <br>
                                            <div class="message" style="display:flex;flex-direction: row;justify-content: space-between;">
                                                <img src="{{user[7]}}" class="post__image__01" />   
                                                <div class="message-box" style="background-color: rgba(34, 33, 33, 0.685);
                                                        color: white;
                                                        padding: 10px 15px;border-radius: 8px;">
                                                    <p>Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum
                                                        Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum
                                                        Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum
                                                        Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum
                                                    </p>
                                                </div>  
                                            </div>
                                        </div>
                                    </div>
                                `;
                            }
                            document.getElementById("timeline").innerHTML = timeline;
                        }
                    })
                });
                    }
                    $(function() {
                        $.ajax({
                            url: '/getfriendrequests',
                            success: function(data) {
                                var friends = Object(data);
                                var fnd = "";
                                for (let i = 0; i < friends["allfriendrequests"].length; i++) {
                                    fnd += `
                                        <div class="friends__link">
                                                <img src="`+friends["allfriendrequests"][i][7]+`" alt="" class="friend__001" />
                                                <h5>`+friends["allfriendrequests"][i][1].split(" ")[0]+`</h5>    
                                                <h5 onclick="requestsFriends('accept','`+friends["allfriendrequests"][i][0]+`');" style="color: blue;margin-top: -2px !important;margin-left: 3px !important;" class="profile__msg"><i class="fa fa-thumbs-up"></i><h5>
                                            <h5 onclick="requestsFriends('reject','`+friends["allfriendrequests"][i][0]+`');" style="color: crimson;margin-top: -2px !important;" class="profile__msg"><i class="fa fa-thumbs-down"></i><h5>
                                                    </div>
                                    `;
                                }
                                if(fnd.length==0){
                                    fnd=`<small style="margin-left: 3rem !important;margin-top: 3rem !important;">No Friends requests till now</small>`;
                                }
                                document.getElementById("frnd__req").innerHTML = fnd;
                            }
                        })
                    });
                    //  Get values of all friends 
                    $(function() {
                    $.ajax({
                        url: '/getfriends',
                        success: function(data) {
                            var friends_ = Object(data);
                            var fnd = "";
                            for (let i = 0; i < friends_["allfriendrequests"].length; i++) {
                                fnd += `
                                    <div class="friends__link__02">
                                            <img src="`+friends_["allfriendrequests"][i][7]+`" alt="" class="friend__001" />
                                            <h5>`+friends_["allfriendrequests"][i][1]+`</h5>    
                                    </div>
                                `;
                            }
                            if(fnd.length==0){
                                fnd=`<small style="margin-left: 3rem !important;margin-top: 3rem !important;">No Friends till now</small>`;
                            }
                            document.getElementById("frnds__lst").innerHTML = fnd;
                        }
                    })
                });
                }
            }
        })
    });
}