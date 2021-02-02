add_action( 'wp_head', function () { ?>
<style>

     /** Container aggregiert Zeilen vertikal **/
    .posts-container {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
            -ms-flex-flow: row wrap;
                flex-flow: row wrap;
        -webkit-box-pack: start;
            -ms-flex-pack: start;
                justify-content: flex-start;
        -webkit-box-align: stretch;
            -ms-flex-align: stretch;
                align-items: stretch;
        
    }
    .posts-container div {
        -webkit-box-sizing: border-box;
                box-sizing: border-box;
    }
	.posts-container a,
	.posts-container a:hover {
		color: white;
	}
    
    .posts-tile {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
            -ms-flex-flow: column nowrap;
                flex-flow: column nowrap;
        -webkit-box-pack: start;
            -ms-flex-pack: start;
                justify-content: flex-start;
        -webkit-box-align: stretch;
            -ms-flex-align: stretch;
                align-items: stretch;
        
        background-color: transparent;
        padding: 10px;
        color: white;
        width: calc( (100% / 3) - (40px / 3) );
        margin-bottom: 20px;
    }
    
    .posts-tile-head-info {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
            -ms-flex-flow: row nowrap;
                flex-flow: row nowrap;
        -webkit-box-pack: justify;
            -ms-flex-pack: justify;
                justify-content: space-between;
        color: #F9D548;
        border-bottom: 2px solid transparent;
        -o-border-image: -o-linear-gradient(left, #F9D548 0%, #d13b75 100%) 1;
           border-image: -webkit-gradient(linear, left top, right top, from(#F9D548), to(#d13b75)) 1;
           border-image: linear-gradient(to right, #F9D548 0%, #d13b75 100%) 1;
        
        padding-bottom: 5px;
    }
	
	.posts-tile-head-info img {
		height: 20px;
	}
    
    .posts-tile-headline {
        margin-top: 20px;
        margin-bottom: 15px;
    }
    
    .posts-tile-headline h3 {
        margin: 0;
        padding: 0;
    }
    
    .posts-tile-excerpt {
        font-size: 14px;
        margin-bottom: 30px;
    }
    
    
    .posts-tile-keyword-cloud {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
            -ms-flex-flow: row wrap;
                flex-flow: row wrap;

    }

    .posts-tile-keyword-cloud > a {
        font-size: 14px;
        margin-right: 30px;
        color: white;
        text-decoration: none;
        border-bottom: 1px solid white;
        padding: 2px 0;

    }
    
    @media (min-width: 1000px) {
        .posts-tile {
            width: calc( (100% / 3) - (40px / 3) );
        }
        
        .posts-tile:nth-child(3n+2) {
            margin-left: 20px;
            margin-right: 20px;
        }
    }
    
    @media (min-width: 768px) and (max-width: 999px) {
         .posts-tile {
            width: calc( (100% / 2) - (20px / 2) );
        }
        
        .posts-tile:nth-child(2n+2) {
            margin-left: 20px;
        }
    }
    
    @media (max-width: 767px) {
        .posts-tile {
            width: 100%;
            margin-bottom: 10px;
        }
    }
	
</style>
<?php } );


/** Custom function um die letzten Posts darzustellen **/

function function_snippet_show_blog_posts( $atts ){
	$a = shortcode_atts( array(
		'anzahl' => 12,
      	'kategorie' => '0'
   ), $atts );
	

	// Ausgabepuffer aktivieren
	ob_start(); 
	
	if( true === is_numeric($a['anzahl']) && 
	   	0 < (int) $a['anzahl'] ) 
	{
		$args = array(
			"posts_per_page" => (int) $a['anzahl'],
			"orderby"        => "date",
			"order"          => "DESC",
			"category"		 => get_cat_ID($a['kategorie'])
		);

		?>
		<div class="posts-container">
			<?php
			$recent_posts = wp_get_recent_posts( $args );
				/** Schleife durch die letzten Posts **/
				if( false === empty($recent_posts) ):
					foreach( $recent_posts as $key => $recent ):
						// Daten auslesen und formatieren
						$date = new DateTime( $recent['post_date'] );
		
						// Kategorie auslesen --> Primäre Kategorie, wenn Yoast Plugin benutzt wird, sonst erste Kategorie
						$primary_category = '';
					 	if (class_exists('WPSEO_Primary_Term')) { 
							$wpseo_primary_term = new WPSEO_Primary_Term( 'category', $recent['ID'] );
							$primary_term 		= get_term( $wpseo_primary_term->get_primary_term() );

							if (!is_wp_error($primary_term) && !empty($primary_term)){
								$primary_category = $primary_term->name;
							} 
						}
						
						if (false === isset($primary_category )) { 
							$primary_category = $a['kategorie'];
						}
		
						// Tags des Posts
						$posttags_string = '';
						$posttags 		 = get_the_tags($recent['ID']);

						if ($posttags) {
							foreach($posttags as $tag) {
								$posttags_string .= '<a href="/?s='. urlencode($tag->name) . '">'. $tag->name .'</a>'; 
						  	}
						}

					?>
					<!-- Erster großer Beitrag-->
			        <?php if ($recent['ID'] > 0) { ?>
					
                        <div class="posts-tile">
                            <div>
                                <!-- Bild über jedem Tile-->
                                    <img src="/wp-content/uploads/2021/01/profie_picture_tso.jpg">
                            </div>

                            <div class="posts-tile-head-info">
                                <div><?php echo $date->format('d.m.Y'); ?> &middot; <?php echo $primary_category; ?></div>
                                <div>
                                    <a href="<?php echo get_permalink($recent['ID']); ?>">
                                        <img src="/wp-content/uploads/2020/12/icon-arrow_right_medium-white-2.svg" alt="Arrow Right" />
                                    </a>
                                </div>
                            </div>
                            <div class="posts-tile-headline">
                                <a href="<?php echo get_permalink($recent['ID']); ?>"><h3><?php echo $recent['post_title']; ?></h3></a>
                            </div>
                            <div class="posts-tile-excerpt">
                                <a href="<?php echo get_permalink($recent['ID']); ?>"><?php echo $recent['post_excerpt'] ?></a>
                            </div>
                            <div class="posts-tile-keyword-cloud">
                                <?php echo $posttags_string; ?>
                            </div>
                        </div>
                    <?php } ?>

					<!-- alle weiteren beiträge-->
			
					
					<div class="posts-tile">
						<div>
							<!-- Bild über jedem Tile-->
								<img src="/wp-content/uploads/2021/01/profie_picture_tso.jpg">
						</div>
						
						<div class="posts-tile-head-info">
							<div><?php echo $date->format('d.m.Y'); ?> &middot; <?php echo $primary_category; ?></div>
							<div>
								<a href="<?php echo get_permalink($recent['ID']); ?>">
									<img src="/wp-content/uploads/2020/12/icon-arrow_right_medium-white-2.svg" alt="Arrow Right" />
								</a>
							</div>
						</div>
						<div class="posts-tile-headline">
							<a href="<?php echo get_permalink($recent['ID']); ?>"><h3><?php echo $recent['post_title']; ?></h3></a>
						</div>
						<div class="posts-tile-excerpt">
							<a href="<?php echo get_permalink($recent['ID']); ?>"><?php echo $recent['post_excerpt'] ?></a>
						</div>
						<div class="posts-tile-keyword-cloud">
							<?php echo $posttags_string; ?>
						</div>
					</div>
			
			
					<?php
					// Ende der Loop durch die Posts
					endforeach;
				
				// Es gibt keine Posts
				else: ?>
					Es gibt leider keine Posts
				<?php
				endif; ?>
		</div><?php // Schließen des Container-Divs
	}
	
	// Ausgabepuffer einlesen
	$ob_str = ob_get_contents();
	
	// Ausgabepuffer leeren
	ob_end_clean();
		
	// Ergebnis zurückgeben
   	return $ob_str;
}
add_shortcode('snippet_show_blog_posts', 'function_snippet_show_blog_posts'); 