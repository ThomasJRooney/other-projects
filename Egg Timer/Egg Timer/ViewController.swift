//
//  ViewController.swift
//  Egg Timer
//
//  Created by Tom Rooney on 10/28/18.
//  Copyright © 2018 Thomas J. Rooney. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var timer = Timer()
    
    var time = 210
    
    @IBOutlet weak var timerLabel: UILabel!
    
    @objc func decreaseTimer() {
        if time > 0 {
            time -= 1
            timerLabel.text = String(time)
        } else {
            timer.invalidate()
        }
    }
    
    @IBAction func playButton(_ sender: Any) {
        timer = Timer.scheduledTimer(timeInterval: 1 , target: self , selector: #selector(ViewController.decreaseTimer), userInfo: nil, repeats: true)
    }
    
    @IBAction func pauseButton(_ sender: Any) {
        timer.invalidate()
    }
    
    @IBAction func minusTen(_ sender: Any) {
        if time > 10 {
            time -= 10
            timerLabel.text = String(time)
        }
    }
    
    @IBAction func plusTen(_ sender: Any) {
        time += 10
        timerLabel.text = String(time)
    }
    
    @IBAction func resetButton(_ sender: Any) {
        time = 210
        timerLabel.text = String(time)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }


}

