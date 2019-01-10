//
//  GameScene.swift
//  Flappy Bird Clone
//
//  Created by Tom Rooney on 11/16/18.
//  Copyright © 2018 Thomas J. Rooney. All rights reserved.
//

import SpriteKit
import GameplayKit

class GameScene: SKScene, SKPhysicsContactDelegate {
    
    var bird = SKSpriteNode()
    
    var bg = SKSpriteNode()
    
    var topPipe = SKSpriteNode()
    
    var bottomPipe = SKSpriteNode()
    
    var gameOver = false
    
    var scoreLabel = SKLabelNode()
    
    var highScoreLabel = SKLabelNode()
    
    var score = 0
    
    var timer = Timer()
    
    var highScore = UserDefaults.standard.integer(forKey: "HIGHSCORE")
    
    enum ColliderType: UInt32 {
        
        case Bird = 1
        case Object = 2
        case Gap = 4
        
    }
    
    @objc func makePipes() {
        //Pipes code
        
        let movePipes = SKAction.move(by: CGVector(dx: -2 * self.frame.width, dy: 0), duration: TimeInterval(self.frame.width / 100))
        
        let gapHeight = bird.size.height * 4
        
        let movementAmount = arc4random() % UInt32(self.frame.height / 2)
        
        let pipeOffset = CGFloat(movementAmount) - self.frame.height/4
        
        let topPipeTexture = SKTexture(imageNamed: "pipe1.png")
        
        topPipe = SKSpriteNode(texture: topPipeTexture)
        
        topPipe.position = CGPoint(x: self.frame.midX + self.frame.width, y: self.frame.midY + topPipeTexture.size().height/2 + gapHeight/2 + pipeOffset)
        
        topPipe.run(movePipes)
        
        topPipe.physicsBody = SKPhysicsBody(rectangleOf: topPipeTexture.size())
        
        topPipe.physicsBody!.isDynamic = false
        
        topPipe.physicsBody!.contactTestBitMask = ColliderType.Object.rawValue
        
        topPipe.physicsBody!.categoryBitMask = ColliderType.Object.rawValue
        
        topPipe.physicsBody!.collisionBitMask = ColliderType.Object.rawValue
        
        self.addChild(topPipe)
        
        let bottomPipeTexture = SKTexture(imageNamed: "pipe2.png")
        
        bottomPipe = SKSpriteNode(texture: bottomPipeTexture)
        
        bottomPipe.position = CGPoint(x: self.frame.midX + self.frame.width, y: self.frame.midY - bottomPipeTexture.size().height / 2 - gapHeight/2 + pipeOffset)
        
        bottomPipe.run(movePipes)
        
        bottomPipe.physicsBody = SKPhysicsBody(rectangleOf: bottomPipeTexture.size())
        
        bottomPipe.physicsBody!.isDynamic = false
        
        bottomPipe.physicsBody!.contactTestBitMask = ColliderType.Object.rawValue
        
        bottomPipe.physicsBody!.categoryBitMask = ColliderType.Object.rawValue
        
        bottomPipe.physicsBody!.collisionBitMask = ColliderType.Object.rawValue
        
        self.addChild(bottomPipe)
        
        let gap = SKNode()
        
        gap.position = CGPoint(x: self.frame.midX + self.frame.width, y: self.frame.midY + pipeOffset)
        
        gap.physicsBody = SKPhysicsBody(rectangleOf: CGSize(width: topPipeTexture.size().width, height: gapHeight))
        
        gap.physicsBody!.isDynamic = false
        
        gap.run(movePipes)
        
        gap.physicsBody!.contactTestBitMask = ColliderType.Bird.rawValue
        
        gap.physicsBody!.categoryBitMask = ColliderType.Gap.rawValue
        
        gap.physicsBody!.collisionBitMask = ColliderType.Gap.rawValue
        
        self.addChild(gap)
        
    }
    
    func didBegin(_ contact: SKPhysicsContact) {
        
        highScoreLabel.text = String(highScore)
        
        if contact.bodyA.categoryBitMask == ColliderType.Gap.rawValue || contact.bodyB.categoryBitMask == ColliderType.Gap.rawValue {
            
            scoreLabel.zPosition = 1
            
            score += 1
            
            scoreLabel.text = String(score)
            

        } else {
       
            self.speed = 0
        
            gameOver = true
            
            timer.invalidate()
            
            let gameOverLabel = SKLabelNode()
            
            gameOverLabel.zPosition = 1
            
            gameOverLabel.fontSize = 50
            
            gameOverLabel.text = "Game Over! Tap to Play Again."
            
            gameOverLabel.position = CGPoint(x: self.frame.midX, y: self.frame.midY)
            
            self.addChild(gameOverLabel)
            
        }
    }
    
    override func didMove(to view: SKView) {
        
        self.physicsWorld.contactDelegate = self
        
        timer = Timer.scheduledTimer(timeInterval: 3.5, target: self, selector: #selector(self.makePipes), userInfo: nil, repeats: true)
        
        //background code
        let bgTexture = SKTexture(imageNamed: "bg.png")
        
        let moveBGAnimation = SKAction.move(by: CGVector(dx: -bgTexture.size().width, dy: 0), duration: 7)
        
        let shiftBGAnimation = SKAction.move(by: CGVector(dx: bgTexture.size().width, dy: 0), duration: 0)
        
        let bgMove = SKAction.repeatForever(SKAction.sequence([moveBGAnimation, shiftBGAnimation]))
        
        var i: CGFloat = 0
        
        while i < 3{
        
            bg = SKSpriteNode(texture: bgTexture)
        
            bg.position = CGPoint(x: bgTexture.size().width * i, y: self.frame.midY)
            
            bg.zPosition = -1
        
            bg.size.height = self.frame.height
        
            bg.run(bgMove)
        
            self.addChild(bg)
            
            i += 1
        }
        
        
        //bird code
        let birdTexture = SKTexture(imageNamed: "flappy1.png")
        
        let birdTexture2 = SKTexture(imageNamed: "flappy2.png")
        
        let animation = SKAction.animate(with: [birdTexture, birdTexture2], timePerFrame: 0.1)
        
        let makeBirdFlap = SKAction.repeatForever(animation)
        
        bird = SKSpriteNode(texture: birdTexture)
        
        bird.position = CGPoint(x: self.frame.midX, y: self.frame.midY)
        
        bird.run(makeBirdFlap)
        
        bird.physicsBody = SKPhysicsBody(circleOfRadius: birdTexture.size().height/2)
        
        bird.physicsBody!.isDynamic = false
        
        bird.physicsBody!.contactTestBitMask = ColliderType.Object.rawValue
        
        bird.physicsBody!.categoryBitMask = ColliderType.Bird.rawValue
        
        bird.physicsBody!.collisionBitMask = ColliderType.Bird.rawValue
        
        self.addChild(bird)
        
        //ground code
        
        let ground = SKNode()
        
        ground.position = CGPoint(x: self.frame.midX, y: -self.frame.height / 2)
        
        ground.physicsBody = SKPhysicsBody(rectangleOf: CGSize(width: self.frame.width , height: 1))
        
        ground.physicsBody!.isDynamic = false
        
        ground.physicsBody!.contactTestBitMask = ColliderType.Object.rawValue
        
        ground.physicsBody!.categoryBitMask = ColliderType.Object.rawValue
        
        ground.physicsBody!.collisionBitMask = ColliderType.Object.rawValue
        
        self.addChild(ground)
        
        scoreLabel.fontName =  "Helvetica"
        
        scoreLabel.fontSize = 100
        
        scoreLabel.text = "0"
        
        scoreLabel.position = CGPoint(x: self.frame.midX - 250, y: self.frame.height / 2 - 130)
        
        self.addChild(scoreLabel)
        
        highScoreLabel.fontName = "Helvetica"
        
        highScoreLabel.zPosition = 1
        
        highScoreLabel.fontSize = 100
        
        highScoreLabel.text = String(highScore)
        
        highScoreLabel.position = CGPoint(x: self.frame.midX + 250, y: self.frame.height / 2 - 130)
        
        self.addChild(highScoreLabel)
        
        if score > UserDefaults.standard.integer(forKey: "HIGHSCORE"){
            
            saveHighScore()
            highScoreLabel.text = String(score)
            
        }
        
    }
    
    
    func setupGame() {
        
        
        timer = Timer.scheduledTimer(timeInterval: 3.5, target: self, selector: #selector(self.makePipes), userInfo: nil, repeats: true)
        
        //background code
        let bgTexture = SKTexture(imageNamed: "bg.png")
        
        let moveBGAnimation = SKAction.move(by: CGVector(dx: -bgTexture.size().width, dy: 0), duration: 7)
        
        let shiftBGAnimation = SKAction.move(by: CGVector(dx: bgTexture.size().width, dy: 0), duration: 0)
        
        let bgMove = SKAction.repeatForever(SKAction.sequence([moveBGAnimation, shiftBGAnimation]))
        
        var i: CGFloat = 0
        
        while i < 3{
            
            bg = SKSpriteNode(texture: bgTexture)
            
            bg.position = CGPoint(x: bgTexture.size().width * i, y: self.frame.midY)
            
            bg.zPosition = -1
            
            bg.size.height = self.frame.height
            
            bg.run(bgMove)
            
            self.addChild(bg)
            
            i += 1
        }
        
        
        //bird code
        let birdTexture = SKTexture(imageNamed: "flappy1.png")
        
        let birdTexture2 = SKTexture(imageNamed: "flappy2.png")
        
        let animation = SKAction.animate(with: [birdTexture, birdTexture2], timePerFrame: 0.1)
        
        let makeBirdFlap = SKAction.repeatForever(animation)
        
        bird = SKSpriteNode(texture: birdTexture)
        
        bird.position = CGPoint(x: self.frame.midX, y: self.frame.midY)
        
        bird.run(makeBirdFlap)
        
        bird.physicsBody = SKPhysicsBody(circleOfRadius: birdTexture.size().height/2)
        
        bird.physicsBody!.isDynamic = false
        
        bird.physicsBody!.contactTestBitMask = ColliderType.Object.rawValue
        
        bird.physicsBody!.categoryBitMask = ColliderType.Bird.rawValue
        
        bird.physicsBody!.collisionBitMask = ColliderType.Bird.rawValue
        
        self.addChild(bird)
        
        //ground code
        
        let ground = SKNode()
        
        ground.position = CGPoint(x: self.frame.midX, y: -self.frame.height / 2)
        
        ground.physicsBody = SKPhysicsBody(rectangleOf: CGSize(width: self.frame.width , height: 1))
        
        ground.physicsBody!.isDynamic = false
        
        ground.physicsBody!.contactTestBitMask = ColliderType.Object.rawValue
        
        ground.physicsBody!.categoryBitMask = ColliderType.Object.rawValue
        
        ground.physicsBody!.collisionBitMask = ColliderType.Object.rawValue
        
        self.addChild(ground)
        
        scoreLabel.fontName =  "Helvetica"
        
        scoreLabel.fontSize = 100
        
        scoreLabel.text = "0"
        
        scoreLabel.position = CGPoint(x: self.frame.midX - 250, y: self.frame.height / 2 - 130)
        
        self.addChild(scoreLabel)
        
        highScoreLabel.fontName = "Helvetica"
        
        highScoreLabel.zPosition = 1
        
        highScoreLabel.fontSize = 100
        
        highScoreLabel.text = String(highScore)
        
        highScoreLabel.position = CGPoint(x: self.frame.midX + 250, y: self.frame.height / 2 - 130)
        
        self.addChild(highScoreLabel)
        
        if score > UserDefaults.standard.integer(forKey: "HIGHSCORE"){
            
            saveHighScore()
            highScoreLabel.text = String(score)
            
        }
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        
        if gameOver == false {
            
        bird.physicsBody!.isDynamic = true
        
        bird.physicsBody!.velocity = CGVector(dx: 0, dy: 0)
        
        bird.physicsBody!.applyImpulse(CGVector(dx: 0, dy: 77))
            
        } else {
            gameOver = false
            
            score = 0
            
            self.speed = 1
            
            self.removeAllChildren()
            
            self.setupGame()
            
        }
        
        if score > UserDefaults.standard.integer(forKey: "HIGHSCORE"){
            
            saveHighScore()
            
        }
        
        }
    
    func saveHighScore() {
        UserDefaults.standard.set(score, forKey: "HIGHSCORE")
    }
    
    override func update(_ currentTime: TimeInterval) {
        // Called before each frame is rendered
    }
}
