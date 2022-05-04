const readMoreBtn = document.querySelector('.read-more-btn');
const text = document.querySelector('.text');

readMoreBtn.addEventListener('click',(e)=>{
    text.classList.toggle('show-more');
    if(readMoreBtn.innerText = 'Read More') {
        readMoreBtn.innerText = 'Read Less';
    } else {
        readMoreBtn.innerText = 'Read More';
    }
})


{/* Butonul de read more, trebuie regandit

<span class="allPosts">
            <?php
                $stmt = $mysql->prepare('SELECT title, selftext FROM `reddit_posts`');
                $stmt->execute();
                $result = $stmt->get_result();
                while ($row = $result->fetch_assoc()):
            ?>
        
            <div class="reddit_post">
                <h3> <?php echo $row['title'] ?> </h3>
                <p class="description"> <?php echo $row['selftext'] ?> </p>
            </div>
            <?php endwhile; ?>
            </span>
            <button class="read-more-btn">Read More</button>
            <script src="./readmore.js"></script> */}